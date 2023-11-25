import React, { useState } from "react";
import axios from "axios";
import { BACKEND_ADDRESS } from "../../config"; // Make sure to create this config file
import "./Login.css";
import email_icon from "../Assets/email.png";
import password_icon from "../Assets/password.png";
import { Link } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      // Define headers
      const headers = {
        "Content-Type": "application/json",
        // Add any other headers you need here
      };

      // User data in JSON format
      const userData = {
        email,
        password,
      };

      // Making the POST request
      const response = await axios.post(`${BACKEND_ADDRESS}/login`, userData, {
        headers,
      });

      console.log(response.data);
      // Handle successful login here (e.g., redirect to dashboard)
    } catch (error) {
      console.error("Error during login:", error);
      // Handle errors here (e.g., show error message)
    }
  };

  return (
    <div className="container">
      <form onSubmit={handleLogin}>
        <div className="header">
          <div className="text">Login</div>
          <div className="underline"></div>
        </div>
        <div className="inputs">
          <div className="input">
            <img src={email_icon} alt="" />
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="input">
            <img src={password_icon} alt="" />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
        </div>
        <div className="forgot-password">
          <span>Forgot Password?</span>
        </div>
        <div className="submit-container">
          <button type="submit" className="submit">
            Login
          </button>
        </div>
        <div className="login">
          <Link to="/">
            <span>Don't have an account? Sign Up</span>
          </Link>
        </div>
      </form>
    </div>
  );
};

export default Login;
