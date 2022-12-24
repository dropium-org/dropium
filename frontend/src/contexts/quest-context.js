import { createContext, useState } from "react";


export const QuestContext = createContext();
export const QuestContextProvider = ({ children }) => {
    const [quest, setQuest] = useState({});
    return (
        <QuestContext.Provider value={{ quest, setQuest }}>{children}</QuestContext.Provider>
    );
}
