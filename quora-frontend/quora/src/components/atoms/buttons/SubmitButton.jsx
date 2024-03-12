// Submit Button component

import React from 'react';

const SubmitButton = (props) => {
    const { text, className } = props;

    return (
        <button
            type="submit"
            className={`bg-blue-500 text-white p-2 rounded-md text-sm ${className || ''}`}
        >
            {text}
        </button>
    );
}

export default SubmitButton;
