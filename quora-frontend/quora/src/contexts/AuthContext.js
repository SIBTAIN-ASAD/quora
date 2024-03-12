// File Contains the context for the authentication of the user. 

import React, { createContext, useState, useEffect } from 'react';

import { fetchUserData } from '../services/authAPIs';

// Create Auth context
export const AuthContext = createContext();

// Auth Provider component
export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        const fetchUser = async () => {

            try {
                const userData = await fetchUserData();
                setUser(userData.user);
            } catch (error) {
                console.error('Error fetching user data:', error.message);
            } finally {
            }
        };

        fetchUser();
    }, []);

    return (
        <AuthContext.Provider
            value={{
                user,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
};
