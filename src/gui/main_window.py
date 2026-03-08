import sys

from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.engine import RetirementInput, calculate_years_to_retirement


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Retirement Calculator")
        self.setMinimumWidth(400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        form_layout = QFormLayout()

        self.current_savings_input = QDoubleSpinBox()
        self.current_savings_input.setRange(0, 100_000_000)
        self.current_savings_input.setDecimals(2)
        self.current_savings_input.setPrefix("$")
        self.current_savings_input.setSingleStep(1000)
        form_layout.addRow("Current Savings:", self.current_savings_input)

        self.annual_savings_input = QDoubleSpinBox()
        self.annual_savings_input.setRange(0, 10_000_000)
        self.annual_savings_input.setDecimals(2)
        self.annual_savings_input.setPrefix("$")
        self.annual_savings_input.setSingleStep(1000)
        form_layout.addRow("Annual Savings:", self.annual_savings_input)

        self.annual_spending_input = QDoubleSpinBox()
        self.annual_spending_input.setRange(1, 10_000_000)
        self.annual_spending_input.setDecimals(2)
        self.annual_spending_input.setPrefix("$")
        self.annual_spending_input.setSingleStep(1000)
        self.annual_spending_input.setValue(40000)
        form_layout.addRow("Annual Spending:", self.annual_spending_input)

        layout.addLayout(form_layout)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)

        layout.addStretch()

    def calculate(self) -> None:
        inputs = RetirementInput(
            current_savings=self.current_savings_input.value(),
            annual_savings=self.annual_savings_input.value(),
            annual_spending=self.annual_spending_input.value(),
        )

        result = calculate_years_to_retirement(inputs)

        if result.years_to_retirement == 0:
            message = (
                f"You're already retired!\n"
                f"Target: ${result.target_amount:,.2f}\n"
                f"Current: ${inputs.current_savings:,.2f}"
            )
        else:
            message = (
                f"Years to retirement: {result.years_to_retirement}\n"
                f"Target amount: ${result.target_amount:,.2f}\n"
                f"Projected final: ${result.final_amount:,.2f}"
            )

        self.result_label.setText(message)


def run_app() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
