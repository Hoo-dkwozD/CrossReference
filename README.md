# CrossReference - CSRF Testing Tool

<p align="center">
    <img src="./static/img/logo.png" />
</p>

A web-based tool for testing Cross-Site Request Forgery (CSRF) vulnerabilities. This application allows users to configure API calls, simulate sequences of requests, and monitor real-time API call logs to identify potential CSRF issues.

## Features

- **Staging Panel**: Configure form fields, define JavaScript functions for API calls, and arrange execution sequences.
- **Testing Panel**: Input test data, run configured sequences, and view detailed API call logs.
- **Real-time Logging**: Track all API requests and responses with timestamps and status information.
- **Vue.js Frontend**: Interactive UI for easy configuration and testing.
- **Flask Backend**: Lightweight Python server for serving the application.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: Vue.js 3, Bulma CSS, Axios
- **Styling**: Custom CSS with Material Icons
- **Code Highlighting**: Highlight.js

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/CrossReference.git
   cd CrossReference
   ```

2. **Install dependencies**:
   ```bash
   pip install Flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to `http://localhost:5000`

## Usage

### Staging Panel
1. **Add Form Fields**: Define input fields that will be used as global variables in your functions.
2. **Create Functions**: Write JavaScript code using the `APICaller()` function (similar to Axios) to make API calls.
3. **Configure Sequence**: Arrange the order in which your functions will execute during testing.
4. **Save Configuration**: Store your setup in localStorage for future sessions.

### Testing Panel
1. **Fill Test Data**: Input values for the configured form fields.
2. **Run Tests**: Execute the sequence of functions and monitor API calls in real-time.
3. **View Logs**: Examine request/response details, including headers, data, and status codes.

## API Caller

The tool provides a global `APICaller` object that wraps Axios with additional features:
- Request/response tracking
- Error handling and logging

Example usage in function code:
```javascript
APICaller.get('https://api.example.com/data')
  .then(response => {
    console.log('Data received:', response.data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

## Configuration

Configurations are automatically saved to localStorage. This includes:
- Form fields
- Functions
- Execution sequence

## Security Note

This tool is intended for educational and testing purposes only. Use it responsibly and only on systems you have permission to test. Always follow ethical hacking guidelines and obtain proper authorization before testing any application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.