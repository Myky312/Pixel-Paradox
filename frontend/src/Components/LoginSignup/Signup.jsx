import React, { useState } from "react";
import axios from "axios";
import "./Signup.css";
import user_icon from "../Assets/person.png";
import email_icon from "../Assets/email.png";
import password_icon from "../Assets/password.png";
import { Link } from "react-router-dom";
import { BACKEND_ADDRESS } from '../../config'; 

const Signup = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async (event) => {
    event.preventDefault();
    try {
      console.log(name, email, password, {BACKEND_ADDRESS});
      const headers = {
        'Content-Type': 'application/json',
        // Add any other headers you need here
      };
  
      // User data in JSON format
      const userData = {
        name,
        email,
        password,
      };
  
      // Making the POST request
      const response = await axios.post(`${BACKEND_ADDRESS}/signup`, userData, { headers });
      console.log(response.data);
      // Handle successful signup here (e.g., redirect to login page)
    } catch (error) {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.error("Error data:", error.response.data);
        console.error("Error status:", error.response.status);
        console.error("Error headers:", error.response.headers);
      } else if (error.request) {
        // The request was made but no response was received
        console.error("Error request:", error.request);
      } else {
        // Something happened in setting up the request that triggered an Error
        console.error('Error', error.message);
      }
    }
  };

  return (
    <div className="container">
        <div className="header">
          <div className="text">Sign Up</div>
          <div className="underline"></div>
        </div>
        <form onSubmit={handleSignup}> {/* Attach the onSubmit event here */}
          <div className="inputs">
            <div className="input">
              <img src={user_icon} alt="" />
              <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
            </div>
            <div className="input">
              <img src={email_icon} alt="" />
              <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </div>
            <div className="input">
              <img src={password_icon} alt="" />
              <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </div>
          </div>
          <div className="login">
            <Link to="/login">
              <span>Already have an Account?</span>
            </Link>
          </div>
          <div className="submit-container">
            <button type="submit" className="submit">Sign Up</button> {/* Removed onSubmit from here */}
          </div>
        </form>
    </div>
  );
};

export default Signup;
