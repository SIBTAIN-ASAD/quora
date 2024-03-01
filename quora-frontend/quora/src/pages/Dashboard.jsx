import React from 'react';
import { useAuth } from '../components/AuthContext';
import './Dashboard.css';

const Dashboard = () => {
    const { currentUser } = useAuth();

    // Redirect to login page if the user is not logged in
    if (!currentUser) {
        window.location.href = '/login';
    }

    const handleLogout = () => {
        // remove the user from local storage and redirect to the login page
        localStorage.removeItem('user');
        window.location.href = '/login';
    }

    return (
        <div className="pic2 min-h-screen flex justify-center items-center bg-gradient-to-b from-purple-400 via-pink-500 to-red-500">
            <div className="container mx-auto w-1/2 p-8 bg-white rounded-lg shadow-lg text-center relative"> {/* Add relative positioning */}
                {currentUser ? (
                    <>
                        <h2 className="text-3xl mt-20 font-bold mb-4 text-gray-900">Hi!
                            <span className="fw-bold text-4xl m-2 text-red-500 ">
                                {currentUser.name}
                            </span>
                        </h2>
                        <div className="user-info border-y-2 p-2 w-72 mx-auto mb-6">
                            <p className="text-gray-800 text-lg animated-text"><strong>Email: </strong> {currentUser.email}</p>
                            <p className="text-gray-800 text-lg ps-0 ms-0 animated-text"><strong>Username: </strong> {currentUser.username}</p>
                            <div className="profile-picture mb-6 absolute top-0 left-1/2 transform -translate-x-1/2"> {/* Add absolute positioning */}
                                {currentUser.profilePicture ? (
                                    <img src={currentUser.profilePicture} alt="Profile" className="-mt-16 rounded-full border-4 border-white" style={{ width: '150px', height: '150px' }} />
                                ) : (
                                    <p className="text-gray-700">No profile picture available</p>
                                )}
                            </div>
                        </div>
                        <button className="bg-red-500 text-white py-3 px-8 rounded-full hover:bg-red-600 focus:outline-none" onClick={handleLogout}>
                            Logout
                        </button>
                    </>
                ) : (
                    <>
                        <h2 className="text-3xl font-bold mb-4 text-gray-900">Welcome to the Dashboard!</h2>
                        <p className="text-gray-700">Please log in to view this page.</p>
                    </>
                )}
            </div>
        </div>
    );
};

export default Dashboard;
