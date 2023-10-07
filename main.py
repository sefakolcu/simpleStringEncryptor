import stringCryption
import stringUncryption

crypted_return = stringCryption.string_cryption_main("HELLO THİS İS SEFA")
print(crypted_return)

uncrypted_return = stringUncryption.string_uncryption_main(crypted_return)

new_crypted_return = stringCryption.string_cryption_password_main("HELO MELO CART CURT", "SEFAK13")
new_uncrypted_return = stringUncryption.string_uncryption_password_main(new_crypted_return, "SEFAK13")
second_uncrypted_return = stringUncryption.string_uncryption_password_main("xWe1rS23yVmNbP53TqV5LpR5rS23yVmNbP53TqV5bQw2aYz1eEmQcqR2TqV5bQw2zCv2eEmQcqR2A9B8pbQSrS23PiQ1aYz1xJ67d8WktqRB", "SEFAK13")

print(new_uncrypted_return)
print(second_uncrypted_return)
