document.addEventListener('DOMContentLoaded', function() {
    const deleteLinks = document.querySelectorAll('a');

    deleteLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to delete this task?')) {
                event.preventDefault();
            }
        });
    });
});
