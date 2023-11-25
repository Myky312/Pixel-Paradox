import React from "react";
import "./Login.css";
import email_icon from "../Assets/email.png";
import password_icon from "../Assets/password.png";
import { Link } from "react-router-dom";

const Login = () => {
  return (
    <div className="container">
      <div className="header">
        <div className="text">Login</div>
        <div className="underline"></div>
      </div>
      <div className="inputs">
        <div className="input">
          <img src={email_icon} alt="" />
          <input type="email" placeholder="Email" />
        </div>
        <div className="input">
          <img src={password_icon} alt="" />
          <input type="password" placeholder="Password" />
        </div>
      </div>
      <div className="forgot-password">
        <span>Forgot Password?</span>
      </div>
      <div className="submit-container">
        <div className="submit">Login</div>
      </div>
      <div className="login">
        <Link to="/">
          <span>Don't have an account? Sign Up</span>
        </Link>
      </div>
    </div>
  );
};

export default Login;
