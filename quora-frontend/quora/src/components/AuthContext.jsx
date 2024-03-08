import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const useAuth = () => {
  return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const refreshAccessToken = useCallback(async () => {
    try {
      const refresh_token = localStorage.getItem('refresh_token');
      if (refresh_token) {
        const response = await axios.post('http://localhost:8000/api/token_refresh', { refresh_token });
        const { access_token } = response.data;
        localStorage.setItem('token', access_token);
      } else {
        console.error('No refresh token available');
        logout();
      }
    } catch (error) {
      console.error('Error refreshing access token:', error.message);
      logout();
    }
  }, []);

  // Run refreshAccessToken every 15 minutes
  useEffect(() => {
    const intervalId = setInterval(refreshAccessToken, 15 * 60 * 1000);

    return () => clearInterval(intervalId); // Cleanup interval on component unmount
  }, [refreshAccessToken]); // Include refreshAccessToken in the dependency array

  const fetchData = useCallback(async () => {
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
      if (error.response && error.response.status === 401) {
        await refreshAccessToken(); // Try refreshing the access token
      }
    } finally {
      setLoading(false);
    }
  }, [setCurrentUser, setLoading, refreshAccessToken]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);


  const login = async (username, password) => {
    try {
      const response = await axios.post('http://localhost:8000/api/login', { username, password });
      const { access_token, refresh_token } = response.data;
      localStorage.setItem('token', access_token);
      localStorage.setItem('refresh_token', refresh_token);
      setCurrentUser(response.data.user);
    } catch (error) {
      console.error('Error logging in:', error.message);
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('refresh_token');
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
