const BASE_URL = "https://a900895c-d0a1-4dbd-a1f8-1c3f7f60be9a.mock.pstmn.io";
export const createQuestAsync = async (data) => fetch(
    `${BASE_URL}/quests`,
    {
        method: "POST",
        body: JSON.stringify(data),
    }
);
