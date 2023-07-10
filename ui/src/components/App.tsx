import { useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import { User } from "../gensrc/api/data-contracts";
import "./App.css";
import AppHeader from "./AppHeader";
import AppFooter from "./AppFooter";
import WorkoutContainer from "./WorkoutContainer";
import Login from "./Login";
import SignUp from "./Signup";

const App = () => {
  const [user, setUser] = useState<User | null>(null);

  return (
    <div className="App">
      <AppHeader />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<WorkoutContainer />} />
          <Route path="/login" element={<Login user={user}/>} />
          <Route path="/signup" element={<SignUp setUser={setUser}/>} />
        </Routes>
      </BrowserRouter>
      <AppFooter />
    </div>
  );
};

export default App;
