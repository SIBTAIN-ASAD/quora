import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux'; // Importing useDispatch and useSelector
import { fetchUserData } from '../../../services/authAPIs';
import { logout } from '../../../services/authAPIs';
import { UserProfile, CommentSection } from '../../page-templates/index';
import { CommentForm } from '../../organisms/index';
import { LogoutButton } from '../../atoms/index';
import './Dashboard.css';

const Dashboard = () => {
    const dispatch = useDispatch(); // Initializing useDispatch hook
    const currentUser = useSelector(state => state.auth.currentUser); // Fetching currentUser from Redux store

    useEffect(() => {
        const fetchData = async () => {
            try {
                dispatch(fetchUserData()); // Dispatching action to fetch user data
            } catch (error) {
                console.error('Error fetching user data:', error.message);
            }
        };

        if (!currentUser) {
            fetchData(); // Fetch user data if currentUser is not available
        }
    }, [dispatch, currentUser]);

    const handleLogout = () => {
        dispatch(logout()); // Dispatching action to log out
    };

    if (!currentUser) {
        window.location.href = '/login';
    }

    return (
        <div className="pic2 min-h-screen flex justify-center items-center bg-gradient-to-b from-purple-400 via-pink-500 to-red-500">
            <div className="container mx-auto w-1/2 p-4 bg-white rounded-lg shadow-lg text-center relative h-5/6">
                <UserProfile />
                <CommentForm />
                <CommentSection />
                <LogoutButton onClick={handleLogout} /> {/* Pass handleLogout as onClick prop */}
            </div>
        </div>
    );
};

export default Dashboard;
