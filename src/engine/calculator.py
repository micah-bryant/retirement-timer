from dataclasses import dataclass

ANNUAL_GROWTH_RATE = 0.07
WITHDRAWAL_RATE = 0.04


@dataclass(frozen=True)
class RetirementInput:
    current_savings: float
    annual_savings: float
    annual_spending: float


@dataclass(frozen=True)
class RetirementResult:
    years_to_retirement: int
    target_amount: float
    final_amount: float


def calculate_retirement_target(annual_spending: float) -> float:
    """Calculate the target retirement savings based on annual spending.

    Uses the 4% safe withdrawal rate rule.
    """
    if annual_spending <= 0:
        raise ValueError("Annual spending must be positive")
    return annual_spending / WITHDRAWAL_RATE


def calculate_years_to_retirement(inputs: RetirementInput) -> RetirementResult:
    """Calculate years until retirement based on savings and spending."""
    if inputs.current_savings < 0:
        raise ValueError("Current savings cannot be negative")
    if inputs.annual_savings < 0:
        raise ValueError("Annual savings cannot be negative")
    if inputs.annual_spending <= 0:
        raise ValueError("Annual spending must be positive")

    target = calculate_retirement_target(inputs.annual_spending)
    savings = inputs.current_savings
    years = 0

    while savings < target:
        savings = savings * (1 + ANNUAL_GROWTH_RATE) + inputs.annual_savings
        years += 1
        if years > 200:
            break

    return RetirementResult(
        years_to_retirement=years,
        target_amount=target,
        final_amount=savings,
    )
