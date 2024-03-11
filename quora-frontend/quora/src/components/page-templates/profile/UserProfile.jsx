// User Profile component

import React from 'react';

import { UserInfoItem, UserProfilePicture } from '../../atoms/index';

const UserProfile = (props) => {

    const currentUser = props.currentUser;

    const profileFields = [
        {
            label: 'Email',
            value: currentUser.email || 'Not available',
        },
        {
            label: 'Username',
            value: currentUser.username || 'Not available',
        },
    ];

    return (
        <>
            <h2 className="text-3xl mt-20 font-bold mb-4 text-gray-900">
                Hi!{' '}
                <span className="fw-bold text-4xl m-2 text-red-500">
                    {currentUser.name}
                </span>
            </h2>
            <div className="user-info border-y-2 p-2 w-72 mx-auto mb-6">
                {profileFields.map((field, index) => (
                    <UserInfoItem
                        key={index}
                        label={field.label}
                        value={field.value}
                    />
                ))}
                <UserProfilePicture profilePicture={currentUser.profile_picture} />
            </div>
        </>
    );
};

export default UserProfile;