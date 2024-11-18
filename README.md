# Broadlink RM Pro AC Controller

This project provides Python scripts to learn and test IR codes for air conditioners using a Broadlink RM Pro device. It's particularly useful for automating AC control through IR commands.

## Features

- Learn IR codes from your AC remote
- Save learned codes to files
- Test saved codes individually or in sequence
- Support for multiple temperature settings (17°C-28°C)
- Retry mechanism for failed command learning
- Interactive command-line interface

## Prerequisites

- Python 3.x
- Broadlink RM Pro device
- Python `broadlink` library

## Installation

1. Clone this repository:
   git clone https://github.com/yourusername/broadlink-ac-controller.git
   cd broadlink-ac-controller

2. Set up a Python virtual environment (recommended):
   python -m venv HA_Venv
   source HA_Venv/bin/activate  # On Windows use: HA_Venv\Scripts\activate

3. Install the required Python package:
   pip install broadlink

## Usage

### Learning IR Codes

Run the learning script to capture IR codes from your AC remote:

python broadlink/learn_ac.py

The script will guide you through:
1. Discovering your RM Pro device on the network
2. Learning IR codes for:
   - Power Off command
   - Cool mode temperatures (17°C through 28°C)
3. Saving codes to individual files in the `codes` directory
4. Retrying any failed command learning attempts

### Testing IR Codes

To test your learned codes:

python broadlink/test_ac.py

The test script provides two options:
1. Test a specific temperature setting
2. Run through all temperatures in sequence (with 5-second delays)

## Project Structure

broadlink-ac-controller/
├── broadlink/
│   ├── learn_ac.py     # IR code learning script
│   ├── test_ac.py      # IR code testing script
│   └── codes/          # Directory containing learned IR codes
│       ├── off.txt
│       ├── cool_17.txt
│       ├── cool_18.txt
│       └── ...
├── HA_Venv/            # Python virtual environment
└── README.md

## How It Works

### Learning Mode
- The `learn_ac.py` script puts the RM Pro into learning mode
- Point your AC remote at the RM Pro device
- Press the desired button on your remote
- The code is captured and saved to a file
- Process repeats for all temperature settings

### Testing Mode
- The `test_ac.py` script reads the saved IR codes
- Sends commands to your AC via the RM Pro
- Allows individual testing or sequential temperature changes

## Troubleshooting

1. Device Not Found
   - Ensure the RM Pro is connected to your network
   - Check if it's powered on and within range
   - Try running the script with admin/sudo privileges

2. Learning Failures
   - Keep the remote very close to the RM Pro (within 10cm)
   - Point directly at the IR receiver
   - Ensure fresh batteries in your remote
   - Use the retry option when prompted

3. Virtual Environment Issues
   - Make sure to activate the virtual environment before running scripts
   - Reinstall dependencies if needed

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using the [python-broadlink](https://github.com/mjg59/python-broadlink) library
- Inspired by home automation needs
- Thanks to the open-source community

## Support

For support, please:
1. Check existing GitHub issues
2. Create a new issue with:
   - Your system details
   - Error messages
   - Steps to reproduce the problem
