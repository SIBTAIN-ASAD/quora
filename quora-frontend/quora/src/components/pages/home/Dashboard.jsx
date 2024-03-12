import React from 'react';
import { useSelector } from 'react-redux';
import { UserProfile, CommentBox } from '../../page-templates/index';
import { LogoutButton } from '../../atoms/index';
import './Dashboard.css';

const Dashboard = () => {

    const data = useSelector((state) => state.user.userDetails);

    // store a copy of the current user
    const currentUser = data;

    if (currentUser === null) {
        // try fetching user details from the server
        window.location.href = '/login';
    }

    return (
        <>
            <div className="pic2 min-h-screen flex justify-center items-center bg-gradient-to-b from-purple-400 via-pink-500 to-red-500">
                <div className="container mx-auto w-1/2 p-4 bg-white rounded-lg shadow-lg text-center relative h-5/6">
                    <UserProfile currentUser={currentUser} />
                    <CommentBox />
                    <LogoutButton />
                </div>
            </div>
        </>
    );
};

export default Dashboard;


