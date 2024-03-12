// File contains the Login form component for the form

import React, { useState } from 'react';

import { Input, SubmitButton } from '../../atoms/index';

const LoginForm = (props) => {

    const { handleSubmit } = props;
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const inputArray = [
        {
            type: 'text',
            name: 'username',
            value: username,
            handleChange: (e) => setUsername(e.target.value),
            placeholder: 'Username',
            required: true,
            className: 'mb-4'
        },
        {
            type: 'password',
            name: 'password',
            value: password,
            handleChange: (e) => setPassword(e.target.value),
            placeholder: 'Password',
            required: true,
            className: 'mb-4'
        }
    ];

    return (
        <form onSubmit={(e) => handleSubmit(e, username, password)}>
            {inputArray.map((input, index) => (
                <Input
                    key={index}
                    type={input.type}
                    name={input.name}
                    value={input.value}
                    handleChange={input.handleChange}
                    placeholder={input.placeholder}
                    required={input.required}
                    className={input.className}
                />
            ))}
            <SubmitButton text="Login" className="mb-6 w-full hover:bg-blue-600" />
        </form>
    );
}

export default LoginForm;
