import pytest

from src.engine.calculator import (
    RetirementInput,
    calculate_retirement_target,
    calculate_years_to_retirement,
)


def test_calculate_retirement_target() -> None:
    """Verify target = spending / 0.04"""
    assert calculate_retirement_target(40000) == 1_000_000
    assert calculate_retirement_target(50000) == 1_250_000
    assert calculate_retirement_target(100000) == 2_500_000


def test_already_retired() -> None:
    """Current savings >= target returns 0 years"""
    inputs = RetirementInput(
        current_savings=1_000_000,
        annual_savings=0,
        annual_spending=40000,
    )
    result = calculate_years_to_retirement(inputs)
    assert result.years_to_retirement == 0
    assert result.target_amount == 1_000_000


def test_basic_calculation() -> None:
    """Known inputs produce expected years"""
    inputs = RetirementInput(
        current_savings=100_000,
        annual_savings=20_000,
        annual_spending=50_000,
    )
    result = calculate_years_to_retirement(inputs)
    assert result.target_amount == 1_250_000
    assert result.years_to_retirement > 0
    assert result.final_amount >= result.target_amount


def test_zero_annual_savings() -> None:
    """Growth only, no contributions"""
    inputs = RetirementInput(
        current_savings=500_000,
        annual_savings=0,
        annual_spending=40_000,
    )
    result = calculate_years_to_retirement(inputs)
    assert result.years_to_retirement > 0
    assert result.final_amount >= result.target_amount


def test_negative_current_savings_raises_error() -> None:
    """Validation rejects negative current savings"""
    inputs = RetirementInput(
        current_savings=-10_000,
        annual_savings=10_000,
        annual_spending=40_000,
    )
    with pytest.raises(ValueError, match="Current savings cannot be negative"):
        calculate_years_to_retirement(inputs)


def test_negative_annual_savings_raises_error() -> None:
    """Validation rejects negative annual savings"""
    inputs = RetirementInput(
        current_savings=10_000,
        annual_savings=-5_000,
        annual_spending=40_000,
    )
    with pytest.raises(ValueError, match="Annual savings cannot be negative"):
        calculate_years_to_retirement(inputs)


def test_zero_spending_raises_error() -> None:
    """Division by zero protection"""
    with pytest.raises(ValueError, match="Annual spending must be positive"):
        calculate_retirement_target(0)

    inputs = RetirementInput(
        current_savings=100_000,
        annual_savings=10_000,
        annual_spending=0,
    )
    with pytest.raises(ValueError, match="Annual spending must be positive"):
        calculate_years_to_retirement(inputs)


def test_negative_spending_raises_error() -> None:
    """Negative spending validation"""
    with pytest.raises(ValueError, match="Annual spending must be positive"):
        calculate_retirement_target(-40_000)
