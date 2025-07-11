from abc import ABC, abstractmethod

class InsurancePolicy(ABC):
    @abstractmethod
    def calculate_premium(self): pass
    @abstractmethod
    def process_claim(self, claim_amount): pass
    @abstractmethod
    def policy_details(self): pass

class LifeInsurance(InsurancePolicy):
    def __init__(self, policy_holder, sum_assured, premium):
        self.policy_holder = policy_holder
        self.sum_assured = sum_assured
        self.premium = premium

    def calculate_premium(self):
        return self.premium

    def process_claim(self, claim_amount):
        if claim_amount <= self.sum_assured:
            return "Claim of {} approved for {}.".format(claim_amount, self.policy_holder)
        return "Claim denied: Exceeds sum assured."

    def policy_details(self):
        return "Life Insurance Policy for {}, Sum Assured: {}, Premium: {}".format(self.policy_holder, self.sum_assured, self.premium)

class AutoInsurance(InsurancePolicy):
    def __init__(self, policy_holder, vehicle_price, premium):
        self.policy_holder = policy_holder
        self.vehicle_price = vehicle_price
        self.premium = premium

    def calculate_premium(self):
        return self.premium

    def process_claim(self, claim_amount):
        if claim_amount <= 0.80 * self.vehicle_price:
            return "Claim of {} approved for {}.".format(claim_amount, self.policy_holder)
        return "Claim denied: Exceeds allowed limit."

    def policy_details(self):
        return "Auto Insurance Policy for {}, Vehicle price: {}, Premium: {}".format(self.policy_holder, self.vehicle_price, self.premium)

class HealthInsurance(InsurancePolicy):
    def __init__(self, policy_holder, coverage_amount, premium):
        self.policy_holder = policy_holder
        self.coverage_amount = coverage_amount
        self.premium = premium

    def calculate_premium(self):
        return self.premium

    def process_claim(self, claim_amount):
        if claim_amount <= self.coverage_amount:
            return "Claim of {} approved for {}.".format(claim_amount, self.policy_holder)
        return "Claim denied: Exceeds coverage amount."

    def policy_details(self):
        return "Health Insurance Policy for {}, Covers: {}, Premium: {}".format(self.policy_holder, self.coverage_amount, self.premium)

def process_insurance(policy):
    print(policy.policy_details())
    print("Premium:", policy.calculate_premium())
    print("Claim Process:", policy.process_claim(50000))
    print()

def test_policies():
    life = LifeInsurance("Alice", 100000, 5000)
    auto = AutoInsurance("Bob", 20000, 1500)
    health = HealthInsurance("Charlie", 75000, 2000)

    assert life.calculate_premium() == 5000
    assert life.process_claim(50000) == "Claim of 50000 approved for Alice."
    assert life.process_claim(150000) == "Denied Exceeds sum assured."

    assert auto.calculate_premium() == 1500
    assert auto.process_claim(15000) == "Claim denied: Exceeds allowed limit."
    assert auto.process_claim(10000) == "Approved for Bob."

    assert health.calculate_premium() == 2000
    assert health.process_claim(50000) == "Claim of 50000 approved for Charlie."
    assert health.process_claim(80000) == "Denied Exceeds coverage amount."

    print("All tests passed successfully!")

if __name__ == "__main__":
    life_policy = LifeInsurance("Alice", 100000, 5000)
    auto_policy = AutoInsurance("Bob", 20000, 1500)
    health_policy = HealthInsurance("Charlie", 75000, 2000)

    for policy in [life_policy, auto_policy, health_policy]:
        process_insurance(policy)

    test_policies()
