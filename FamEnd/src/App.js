import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8080')
        .then(response => response.json())
        .then(data => setMessage(data.message));
  }, []);

  return (
    <div className="App">
        <header className="App-header">
            { message ? <p>{message}</p> : <p>Loading...</p> }
        </header>
    </div>
  );
}

export default App;
