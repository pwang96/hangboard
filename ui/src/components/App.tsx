import { useState } from 'react';

import './App.css';
import AppHeader from './AppHeader';
import MessageBox from './MessageBox';

const App = () => {

  return (
    <div className="App">
      <AppHeader />
      <div>
        <MessageBox/>
      </div>
    </div>
  );
}

export default App;
