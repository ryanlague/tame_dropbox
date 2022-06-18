# Dropbox Tamer

When Dropbox is syncing, it can use up all your CPU very quickly. Especially on a laptop, 
the machine can get very hot and very slow.

![Dropbox devours CPU](https://github.com/ryanlague/tame-dropbox.git/img/1_dropbox_195.png)

This simple script limits the amount of CPU that Dropbox is allowed to use, so your computer remains useable while 
Dropbox is syncing.

![Dropbox Tamer set to 40%](https://github.com/ryanlague/tame-dropbox.git/img/1_dropbox_39.png)


## Installation

### GitHub
```bash
clone https://github.com/ryanlague/tame-dropbox.git
cd tame_dropbox/tame_dropbox
```

## Usage

### CLI
```bash
# Only allow Dropbox to use 40% of the CPU
sudo python3 main.py -p 40

# Kill Dropbox Tamer, allowing Dropbox to use all the CPU it wants (as usual)
sudo python3 main.py --kill
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) 2022 Ryan Lague

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.