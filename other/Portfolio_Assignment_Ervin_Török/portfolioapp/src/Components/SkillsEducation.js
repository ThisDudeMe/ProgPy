import React from 'react'
import styles from '../Modules/SkillsEducation.module.css'

export const SkillsEducation = () => {
    return (
        <div className={styles.skillsEducationContainer}>
            <div className={styles.educationContainer}>
                <div className={styles.educationTitle}>

                    Education

                </div>

                <div className={styles.educationContent}>

                    School_PH
                    School_PH
                    School_PH

                </div>
            </div>

            <div className={styles.workContainer}>
                <div className={styles.workTitle}>

                    Work Experience

                </div>

                <div className={styles.workContent}>

                    Work_PH
                    Work_PH
                    Work_PH

                </div>
            </div>

            <div className={styles.programingLanguageContainer}>
                <div className={styles.programingLanguageTitle}>

                    ProgramingLanguage

                </div>

                <div className={styles.programingLanguageContent}>

                    ProgramingLanguage_PH
                    ProgramingLanguage_PH
                    ProgramingLanguage_PH

                </div>
            </div>

            <div className={styles.languageContainer}>
                <div className={styles.languageTitle}>

                    Language

                </div>

                <div className={styles.languageContent}>

                    Language_PH
                    Language_PH
                    Language_PH

                </div>
            </div>
        </div>
    )
}
