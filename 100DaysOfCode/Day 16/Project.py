from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirt", "charmander"], "l")
table.add_column("type", ["Electric", "Water", "Fire"], "l")
print(table)