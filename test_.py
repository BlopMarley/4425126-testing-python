import pytest
from source import reverse_str
from calculate.operators import Operators
from calculate.view import View

def test_should_reverse_string():
    assert reverse_str('abc') == 'cba'

def test_should_make_multiple_addition():
    sut = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected_value = 59.2
    assert sut.addition(operation) == expected_value

def test_should_make_addition():
    sut = Operators()
    operation = "5.5 + 10"
    expected_value = 15.5
    assert sut.addition(operation) == expected_value

def test_addition_should_return_none_with_wrong_operator():
    sut = Operators()
    operation = "5.5 * 10"
    expected_value = None
    assert sut.addition(operation) == expected_value

def test_addition_should_return_none_with_wrong_operation():
    sut = Operators()
    operation = "5.5 + 10 - 10"
    expected_value = None
    assert sut.addition(operation) == expected_value


def test_addition_should_return_none_with_non_digit_symbol():
    sut = Operators()
    operation = "5.5 + 10 + A"
    expected_value = None
    assert sut.addition(operation) == expected_value


def test_should_make_substraction():
    sut = Operators()
    operation = "5.5 - 10"
    expected_value = -4.5
    assert sut.substraction(operation) == expected_value


def test_should_make_multiple_substraction():
    sut = Operators()
    operation = "5.5 - 10 - 30 - 13.7"
    expected_value = -48.2
    assert sut.substraction(operation) == expected_value


def test_substraction_should_return_none_with_wrong_operator():
    sut = Operators()
    operation = "5.5 * 10"
    expected_value = None
    assert sut.substraction(operation) == expected_value


def test_substraction_should_return_none_with_wrong_operation():
    sut = Operators()
    operation = "5.5 + 10 - 10"
    expected_value = None
    assert sut.substraction(operation) == expected_value


def test_substraction_should_return_none_with_non_digit_symbol():
    sut = Operators()
    operation = "5.5 - 10 - A"
    expected_value = None
    assert sut.substraction(operation) == expected_value


def test_should_make_multiplication():
    sut = Operators()
    operation = "5.5 * 10"
    expected_value = 55.0
    assert sut.multiplication(operation) == expected_value


def test_should_make_multiple_multiplication():
    sut = Operators()
    operation = "5.5 * 10 * 30 * 13.7"
    expected_value = 22605.0
    assert sut.multiplication(operation) == expected_value


def test_multiplication_should_return_none_with_wrong_operator():
    sut = Operators()
    operation = "5.5 / 10"
    expected_value = None
    assert sut.multiplication(operation) == expected_value


def test_multiplication_should_return_none_with_wrong_operation():
    sut = Operators()
    operation = "5.5 * 10 - 10"
    expected_value = None
    assert sut.multiplication(operation) == expected_value


def test_multiplication_should_return_none_with_non_digit_symbol():
    sut = Operators()
    operation = "5.5 * 10 * A"
    expected_value = None
    assert sut.multiplication(operation) == expected_value


def test_should_make_division():
    sut = Operators()
    operation = "5.5 / 10"
    expected_value = 0.55
    assert sut.division(operation) == pytest.approx(expected_value)


def test_should_make_multiple_division():
    sut = Operators()
    operation = "5.5 / 10 / 10"
    expected_value = 0.055
    assert sut.division(operation) == pytest.approx(expected_value)


def test_division_should_return_none_with_wrong_operator():
    sut = Operators()
    operation = "5.5 * 10"
    expected_value = None
    assert sut.division(operation) == expected_value


def test_division_should_return_none_with_wrong_operation():
    sut = Operators()
    operation = "5.5 / 10 - 10"
    expected_value = None
    assert sut.division(operation) == expected_value


def test_division_should_return_none_with_zero_division():
    sut = Operators()
    operation = "5.5 / 0"
    expected_value = None
    assert sut.division(operation) == expected_value

def test_should_print_menu(capsys):
    View.print_menu()
    out, err = capsys.readouterr()
    expect_out = ("\n=========== MENU ==========="
                  "\n1 - Addition"
                  "\n2 - Soustraction"
                  "\n3 - Multiplication"
                  "\n4 - Division"
                  "\n5 - Quitter"
                  "\n============================\n\n")
    assert out == expect_out


def test_should_print_end_message(capsys):
    View.end_message()
    out, err = capsys.readouterr()
    expect_out = "=========== GOOD-BYE ===========\n"
    assert out == expect_out


def test_should_print_result(capsys):
    operation = "5+10"
    result = 15
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    expect_out = f"RESULTAT : {operation} = {result}\n"
    assert out == expect_out


def test_should_print_result_with_error(capsys):
    operation = "5+10+A"
    result = None
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    expect_out = f"Votre operation est incorrect ! : {operation}\n"
    assert out == expect_out