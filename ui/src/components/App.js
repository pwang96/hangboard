import { useState } from 'react';

import './App.css';
import MessageBox from './MessageBox';

const App = () => {
  const [lastMessage, setLastMessage] = useState("hello world");

  return (
    <div className="App">
      <header className="App-header">
        <MessageBox/>
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <div>
          <p>
            {lastMessage}
          </p>
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
