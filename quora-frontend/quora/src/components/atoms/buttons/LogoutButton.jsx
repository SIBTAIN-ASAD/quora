// This file contains the logout Button for the App

import React from 'react';
import { logout } from '../../../services/authAPIs';

const LogoutButton = () => {

    const handleLogout = () => {
        logout();
        window.location.href = '/login';
    }

    return (
        <button className="bg-red-500 my-4 text-white py-2 px-6 rounded-full hover:bg-red-600 focus:outline-none" onClick={handleLogout}>
            Logout
        </button>
    );
}

export default LogoutButton;
