#!/usr/bin/env python3

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
from termcolor import colored


x = int(input("Masukkan jumlah: "))
i = 1
# Generate english mnemonic words
MNEMONIC: str = generate_mnemonic(language="english", strength=128)
# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # "meherett"

# Initialize Ethereum mainnet BIP44HDWallet
bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
# Get Ethereum BIP44HDWallet from mnemonic
bip44_hdwallet.from_mnemonic(
    mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE
)
# Clean default BIP44 derivation indexes/paths
bip44_hdwallet.clean_derivation()

print("\nMnemonic\t:\n\n",(colored(bip44_hdwallet.mnemonic(),"green")),"\n")
#print("Base HD Path:  m/44'/60'/0'/0/{address_index}", "\n")

# Get Ethereum BIP44HDWallet information's from address index
for address_index in range(x):
    # Derivation from Ethereum BIP44 derivation path
    bip44_derivation: BIP44Derivation = BIP44Derivation(
        cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
    )
    # Drive Ethereum BIP44HDWallet
    bip44_hdwallet.from_path(path=bip44_derivation)
    # Print address_index, path, address and private_key
    print(f"{i}. Address\t:\n{bip44_hdwallet.address()}\nPrivatekey\t:\n0x{bip44_hdwallet.private_key()}")
    i = i + 1
    # Clean derivation indexes/paths
    bip44_hdwallet.clean_derivation()
    
    


