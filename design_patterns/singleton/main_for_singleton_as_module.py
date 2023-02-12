from singleton_as_module import singleton
from singleton_as_module import SingletonAsModule
import main_for_singleton_as_module_second

print(singleton, id(singleton))
print(singleton, id(singleton))

s = SingletonAsModule()
print(s, id(s))