// User Profile Picture component
import React from 'react';

const UserProfilePicture = (props) => {

    const { profilePicture } = props;

    return (
        <div className="profile-picture mb-6 absolute top-0 left-1/2 transform -translate-x-1/2">
            {profilePicture ? (
                <img
                    src={profilePicture}
                    alt="ProfilePicture"
                    className="-mt-16 rounded-full border-4 border-white"
                    style={{ width: '150px', height: '150px' }}
                />
            ) : (
                <p className="text-gray-700">No profile picture available</p>
            )}
        </div>
    );
}

export default UserProfilePicture;
