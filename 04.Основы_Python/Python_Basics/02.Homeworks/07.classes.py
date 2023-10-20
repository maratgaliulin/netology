from classes.rate import Rate
from classes.currency_codes import CurrencyCodes
from classes.developer import Developer
from classes.designer import Designer

# Rate:
# rate_instance = Rate(diff=True)
# cc = CurrencyCodes()
# rate_instance.format = 'value'
# print(rate_instance.make_format('USD'))


# Employee
# alex = Developer('Александр', 0)#
# for i in range(20):
#     alex.check_if_it_is_time_to_upgrade()
jack = Designer('Jack', 4)

print(f' Seniority: {jack.seniority}')

jack.check_if_it_is_time_to_upgrade(award=False)
jack.check_if_it_is_time_to_upgrade(award=False)
jack.check_if_it_is_time_to_upgrade(award=True)
jack.check_if_it_is_time_to_upgrade(award=True)
print(f' Seniority: {jack.seniority}')

# print(rate_instance.usd())
# print(cc.currency_id('USD'))

