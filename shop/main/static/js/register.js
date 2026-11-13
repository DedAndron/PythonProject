const form = document.getElementById('registerForm');

form.addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(form);

    try {
        const response = await fetch("{% url 'register' %}", {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            window.location.href = result.redirect_url;
        } else {
            alert(result.error || 'Registration failed!');
        }

    } catch (error) {
        console.error('Registration error:', error);
        alert('Something went wrong!');
    }
});