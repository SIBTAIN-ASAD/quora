// AuthProvider.js
import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const useAuth = () => {
  return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem('token');
        if (token) {
          const response = await axios.get('http://localhost:8000/api/home', {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          setCurrentUser(response.data);
        }
      } catch (error) {
        console.error('Error fetching user data:', error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const login = async (username, password) => {
    try {
      const response = await axios.post('http://localhost:8000/api/login', { username, password });
      const { access_token } = response.data;
      localStorage.setItem('token', access_token);
      setCurrentUser(response.data.user);
    } catch (error) {
      console.error('Error logging in:', error.message);
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setCurrentUser(null);
  };

  const value = {
    currentUser,
    login,
    logout,
  };

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
};
