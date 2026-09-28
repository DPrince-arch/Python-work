import ast
import re
import basic
import scientific as sci
import trigonometric as trig
import constants
import Modes
import Modes.vector as vector
import Modes.central_tendency as central_tendency
import Modes.matrix as matrix
import Modes.equations as equations
import Modes.complex as complex
import Modes.central_tendency as central_tendency
import Modes.statistics as statistics
import Modes.Bases.binary as binary
import Modes.Bases.octal as octal
import Modes.Bases.hexadecimal as hexadecimal
import Modes.Bases.other as other
import Modes.convert as convert

_ALLOWED_NAMES = {
    "rt": sci.square_root,
    "cbrt": sci.cube_root,
    "fact": sci.factorial,
    "ln": sci.natural_log,
    "log10": sci.log_base_10,
    "log": sci.log_base_n,
    "exp": sci.exponential,
    "sin": trig.sin_deg,
    "cos": trig.cos_deg,
    "tan": trig.tan_deg,
    "asin": trig.asin_deg,
    "acos": trig.acos_deg,
    "atan": trig.atan_deg,
    "pi": constants.PI,
    "e": constants.E,
    "mode": Modes,
    "vec_add": vector.vector_addition,
    "vec_sub": vector.vector_subtraction,
    "vec_dot": vector.vector_dot_product,
    "vec_cross": vector.vector_cross_product,
    "vec_mag": vector.vector_magnitude,
    "vec_norm": vector.vector_normalization,
    "vec_angle": vector.vector_angle,
    "vec_proj": vector.vector_projection,
    "mean": central_tendency.mean,
    "variance": statistics.variance,
    "std_dev": statistics.standard_deviation,
    "mean_dev": statistics.mean_deviation,
    "iqr": statistics.interquartile_range,
    "cv": statistics.coefficient_of_variation,
    "mad": statistics.mean_absolute_deviation,
    "mat_add": matrix.matrix_addition,
    "mat_sub": matrix.matrix_subtraction,
    "mat_mul": matrix.matrix_multiplication,
    "mat_trans": matrix.matrix_transpose,
    "det": matrix.determinant,
    "mat_inv": matrix.inverse,
    "lin_eq": equations.linear_equation,
    "quad_eq": equations.quadratic_equation,
    "cubic_eq": equations.cubic_equation,
    "complex_add": complex.complex_addition,
    "complex_sub": complex.complex_subtraction,
    "complex_mul": complex.complex_multiplication,
    "complex_div": complex.complex_division,
    "median": central_tendency.median,
    "mode": central_tendency.mode,
    "bin_to_dec": binary.binary_to_decimal,
    "dec_to_bin": binary.decimal_to_binary,
    "bin_to_oct": binary.binary_to_octal,
    "bin_to_hex": binary.binary_to_hexadecimal,
    "bin_add": binary.binary_addition,
    "bin_sub": binary.binary_subtraction,
    "bin_mul": binary.binary_multiplication,
    "bin_div": binary.binary_division,
    "bin_mod": binary.binary_modulus,
    "bin_pow": binary.binary_power,
    "oct_to_dec": octal.octal_to_decimal,
    "dec_to_oct": octal.decimal_to_octal,
    "oct_to_hex": octal.octal_to_hexadecimal,
    "oct_to_bin": octal.octal_to_binary,
    "oct_add": octal.octal_addition,
    "oct_sub": octal.octal_subtraction,
    "oct_mul": octal.octal_multiplication,
    "oct_div": octal.octal_division,
    "oct_mod": octal.octal_modulus,
    "oct_pow": octal.octal_power,
    "hex_to_dec": hexadecimal.hexadecimal_to_decimal,
    "dec_to_hex": hexadecimal.decimal_to_hexadecimal,
    "hex_to_bin": hexadecimal.hexadecimal_to_binary,
    "hex_to_oct": hexadecimal.hexadecimal_to_octal,
    "hex_add": hexadecimal.hexadecimal_addition,
    "hex_sub": hexadecimal.hexadecimal_subtraction,
    "hex_mul": hexadecimal.hexadecimal_multiplication,
    "hex_div": hexadecimal.hexadecimal_division,
    "hex_mod": hexadecimal.hexadecimal_modulus,
    "hex_pow": hexadecimal.hexadecimal_power,
    "base_to_base": other.base_conversion,
    "convert": convert.conversion,
}

_ALLOWED_NODES = (
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.Call, ast.Name, ast.Load,
    ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow,
    ast.USub, ast.UAdd,
)


def convert_factorials(s: str) -> str:
    while "!" in s:
        idx = s.index("!")
        j = idx - 1
        if j >= 0 and s[j] == ")":
            depth = 1
            k = j - 1
            while k >= 0 and depth > 0:
                if s[k] == ")":
                    depth += 1
                elif s[k] == "(":
                    depth -= 1
                k -= 1
            start = k + 1
            operand = s[start:idx] 
            s = s[:start] + "fact" + operand + s[idx + 1:]
        else:
            k = j
            while k >= 0 and (s[k].isdigit() or s[k] == "."):
                k -= 1
            start = k + 1
            operand = s[start:idx]
            if not operand:
                raise ValueError("'!' must follow a number or parenthesized expression.")
            s = s[:start] + "fact(" + operand + ")" + s[idx + 1:]
    return s


def validate(node, allowed_names):
    if not isinstance(node, _ALLOWED_NODES):
        raise ValueError(f"Disallowed expression element: {type(node).__name__}")

    if isinstance(node, ast.Name) and node.id not in allowed_names:
        raise ValueError(f"Unknown name: '{node.id}'")
        
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name) or node.func.id not in allowed_names:
            raise ValueError("Only whitelisted functions may be called.")

    for child in ast.iter_child_nodes(node):
        validate(child, allowed_names)


def evaluate(expression: str, ans=None):
    expression = expression.replace("^", "**")

    expression = convert_factorials(expression)

    names = dict(_ALLOWED_NAMES)
    if ans is not None:
        names["ans"] = ans

    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"Invalid expression syntax: {e}")

    validate(tree, names)

    code = compile(tree, "<expression>", "eval")
    return eval(code, {"__builtins__": {}}, names)