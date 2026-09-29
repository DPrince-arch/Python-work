from typing import AsyncGenerator, List, Dict, Optional
from app.config import settings
from app.prompts import SOCRATIC_DOCUMENT_SYSTEM_PROMPT, SOCRATIC_TOPIC_SYSTEM_PROMPT
from services.rag_service import rag_service

class SocraticService:
    def __init__(self):
        pass

    async def stream_socratic_response(
        self,
        document_id: Optional[str],
        topic_name: Optional[str],
        user_message: str,
        history: List[Dict[str, str]],
        api_key: Optional[str] = None,
    ) -> AsyncGenerator[str, None]:

        if document_id:
            chunks = rag_service.get_relevant_chunks(document_id, user_message, top_k=3, api_key=api_key)
            context_str = "\n---\n".join(chunks) if chunks else "No document chunks retrieved."
            system_instruction = SOCRATIC_DOCUMENT_SYSTEM_PROMPT.format(context=context_str)
        elif topic_name:
            system_instruction = SOCRATIC_TOPIC_SYSTEM_PROMPT.format(topic_name=topic_name)
        else:
            system_instruction = SOCRATIC_TOPIC_SYSTEM_PROMPT.format(topic_name="General Knowledge")

        resolved_gemini_key = settings.get_api_key("socratic", api_key)

        if resolved_gemini_key:
            try:
                from google import genai
                from google.genai import types

                client = genai.Client(api_key=resolved_gemini_key)
                
                contents = []
                for msg in history[-settings.MAX_HISTORY_MESSAGES:]:
                    contents.append(
                        types.Content(
                            role=msg["role"],
                            parts=[types.Part.from_text(text=msg["content"])]
                        )
                    )
                contents.append(
                    types.Content(
                        role="user",
                        parts=[types.Part.from_text(text=user_message)]
                    )
                )

                config = types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7,
                )

                response_stream = client.models.generate_content_stream(
                    model=settings.MODEL_NAME,
                    contents=contents,
                    config=config,
                )

                for chunk in response_stream:
                    if chunk.text:
                        yield f"data: {chunk.text}\n\n"
                
                yield "data: [DONE]\n\n"
                return
            except Exception as e:
                print(f"[SocraticService] Error streaming from Gemini API: {e}")

        topic = topic_name or "this topic"
        fallback_text = (
            f"That's a great initial thought regarding {topic}! "
            f"To help you discover the core principle here, what do you think happens when we look at the underlying rules of {topic}?"
        )
        
        words = fallback_text.split(" ")
        for word in words:
            yield f"data: {word} \n\n"
            import asyncio
            await asyncio.sleep(0.04)

        yield "data: [DONE]\n\n"

socratic_service = SocraticService()
