// Form for adding a comment
import React, { useState } from "react";


import { postCommet } from "../../../services/commentAPIS";
import { Input, Textarea, SubmitButton } from "../../atoms/index";

const CommentForm = () => {

    // State to hold the form data
    const [commentData, setCommentData] = useState({
        rating: '',
        catalog: '',
        review: '',
        comment_type: '',
        comment: ''
    });

    // Input fields for the form
    const inputFields = [
        { type: "text", name: "rating", placeholder: "Rating" },
        { type: "text", name: "catalog", placeholder: "Catalog" },
        { type: "text", name: "review", placeholder: "Review" },
        { type: "text", name: "comment_type", placeholder: "Comment Type" }
    ];

    // Function to handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        await postCommet(commentData);

        // Clear the form
        for (const key in commentData) {
            setCommentData({
                ...commentData,
                [key]: ''
            });
        }
    };

    // Function to handle input changes
    const handleChange = (e) => {
        const { name, value } = e.target;
        setCommentData({
            ...commentData,
            [name]: value
        });
    };


    return (
        <form onSubmit={handleSubmit} className="mt-4 h-auto overflow-auto">
            <div className="grid grid-cols-2 gap-1">
                {inputFields.map((field, index) => (
                    <Input
                        key={index}
                        type={field.type}
                        name={field.name}
                        placeholder={field.placeholder}
                        onChange={handleChange}
                    />
                ))}
                <Textarea
                    name="comment"
                    value={commentData.comment}
                    placeholder="Comment"
                    onChange={handleChange}
                />
                <SubmitButton text="Add Comment" />
            </div>
        </form>
    );
};

export default CommentForm;
