# RSA Module

## Description
RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem, one of the oldest, that is widely used for secure data transmission.
In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret. The public
key is based on 2 large prime numbers, thus the difficulty of breaking/decoding the message lies in finding the correct factoring 
of those 2 large prime numbers.

In these scripts, I tried to implement both the classical RSA and RSA with padding for each block in message. For now, it works  
only with small bit keys, but I plan to learn to make it more efficient in the future.

## Tools and technologies learned

- python bit operations
- RSA algorithm

## Installation and run

Simply clone the repo, prepare your Python environment (math, utils and random libraries were used, so most modern Python versions 
should work) and run the main.py script in it.

Example using Anaconda -> Open cmd terminal and type:
```
conda create --name *yourEnvironmentName* python=3.10

cd *pathToFolderWhereYouClonedIt*

activate yourEnvironmentName

python main.py
```

If it takes too long and you want to stop the process, in the same terminal, use CTRL+D key combination.

If you want to deactivate the conda environment, in the terminal type:
```
conda deactivate *yourEnvironmentName*
```

## Visuals

### RSA with padding
![SSRSAPadding](screenshots%2FSSRSAPadding.png)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Feel free to contact me at: karjhan1999@gmail.com