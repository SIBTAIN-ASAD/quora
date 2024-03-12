import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./authentications/Login";
import Dashboard from "./home/Dashboard";
const App = () => {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
