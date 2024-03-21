import React from 'react';
import style from '../Modules/ReferencesContact.module.css';

export const ReferencesContact = () => {
    return (
        <div className={style.referencesContactContainer}>
            <div className={style.referencesContainer}>
                <div className={style.referencesTitle}>
                    References
                </div>

                <div className={style.referencesContent}>

                    reference1
                    reference 2

                </div>
            </div>

            <div className={style.contactMeContainer}>
                <div className={style.contactMeTitle}>
                    Contact Me
                </div>

                <div className={style.contactMeContent}>

                    LinkedIn
                    Email
                    Tel

                </div>
            </div>

            <div className={style.contactFormContainer}>
                <div className={style.contactFormTitle}>
                    Contact Form
                </div>

                <div className={style.contactFormContent}>
                    <div>
                        <div>

                            <input type="text" name="email" id="email" placeholder="Email" />

                        </div>

                        <div>

                            <input type="text" name="name" id="name" placeholder="Name" />

                        </div>

                        <div>

                            <textarea name="freetext" id="freetext" cols="30" rows="10" placeholder="Enter your message"></textarea>

                        </div>
                    </div>
                </div>
            </div>

        </div>
    );
};
