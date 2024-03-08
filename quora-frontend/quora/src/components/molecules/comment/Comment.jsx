// Comment component to display a single comment

import React from 'react';

import { DeleteButton } from '../../atoms';

const Comment = (props) => {

    const { comment, onDelete } = props;

    // Get all keys of the comment object
    const commentKeys = Object.keys(comment);

    return (
        <div className="bg-gray-100 rounded-md mb-2">
            <div className='flex flex-col justify-start text-left'>
                {commentKeys.map((key, index) => (
                    <p key={index}>
                        {key}: {comment[key]}
                    </p>
                ))}
            </div>
            <DeleteButton onClick={() => onDelete(comment.id)} />
        </div>
    );
};

export default Comment;
