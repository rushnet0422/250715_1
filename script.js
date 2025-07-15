// script.js
// Gemini API 연동 예시 (실제 API 키와 엔드포인트는 별도 서버에서 처리 권장)

document.getElementById('activityForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const subject = document.getElementById('subject').value;
    const activity = document.getElementById('activity').value;
    const resultDiv = document.getElementById('result');

    resultDiv.textContent = '변환 중...';

    // 실제 서비스에서는 서버에서 Gemini API 호출 권장
    // 아래는 예시용 fetch 코드 (API 키 노출 위험)
    try {
        // 예시: 서버에 POST 요청 (서버에서 Gemini API 호출)
        const response = await fetch('http://localhost:5000/gemini-convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ subject, activity })
        });
        if (!response.ok) throw new Error('서버 오류');
        const data = await response.json();
        resultDiv.textContent = data.result || '결과를 받아올 수 없습니다.';
    } catch (err) {
        resultDiv.textContent = '오류 발생: ' + err.message;
    }
});
