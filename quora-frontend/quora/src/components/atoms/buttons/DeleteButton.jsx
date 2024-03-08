// Delete button component

import React from 'react';

const DeleteButton = (props) => {

    const { onClick } = props;

    return (
        <button onClick={onClick} className="text-red-500 hover:text-red-700">
            Remove
        </button>
    );
};

export default DeleteButton;
