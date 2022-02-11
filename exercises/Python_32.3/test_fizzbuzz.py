import pytest
from fizzbuzz import fizzbuzz

def test_is_fizzbuzz_retun_response_type_list():
  'Para o retorno da função com tipo lista'
  assert type(fizzbuzz(5)) is list

def test_is_fizzbuzz_type_string_params_raises_an_exception():
  'Para execeção ao receber string como paramentro'
  with pytest.raises(TypeError, match = r'can only concatenate str \(not "int"\) to str'):
    fizzbuzz('a')

def test_is_fizzbuzz_param_four_not_includes_buzz():
  'Para um parametro 4 não inclui Buzz'
  assert not ('Buzz' in fizzbuzz(4)) is True

def test_is_fizzbuzz_param_four_not_includes_fizzbuzz():
  'Para um parametro 4 não inclui FizzBuzz'
  assert not ('FizzBuzz' in fizzbuzz(4)) is True

def test_is_fizzbuzz_param_ten_not_includes_fizzbuzz():
  'Para um parametro 10 não inclui FizzBuzz'
  assert not ('FizzBuzz' in fizzbuzz(10)) is True

def test_is_fizzbuzz_param_fifteen_includes_fizzbuzz():
  'Para um parametro 15 inclui FizzBuzz'
  assert ('FizzBuzz' in fizzbuzz(15)) is True