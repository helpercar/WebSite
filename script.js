async function fetchBlogPosts() {
    const container = document.getElementById('blogContainer');
    
    // Just so that other pages don't use this code
    if (!container) {
        console.log("Returning");
        return; 
    }

    const siteUrl = 'https://public-api.wordpress.com';
    const endpoint = `${siteUrl}/rest/v1/sites/helpercarsblog.wordpress.com/posts/`;

    try {
        const response = await fetch(endpoint);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log(data);
        const posts = data.posts; 
        
        // Clear text
        container.innerHTML = ''; 

        // Loop through the array of articles returned
        posts.forEach(post => {
            const article = document.createElement('article');
            article.className = 'blog-post-card';
            
            // Format and inject the specific raw post components into an HTML layout
            article.innerHTML = `
                <h2 class="blog-title">${post.title}</h2>
                <div class="blog-meta">Published on ${new Date(post.date).toLocaleDateString()}</div>
                <div class="blog-excerpt">${post.excerpt}</div>
                <a href="${post.URL}" target="_blank" class="read-more-btn">Read Full Article</a>
                <hr class="blog-divider">
            `;
            container.appendChild(article);
        });
    } catch (error) {
        console.error('Error fetching blog posts:', error);
        container.innerText = 'Unable to load articles at this time.';
    }
}

// Unfortunately, due to the templates, this will be ran on every page, but we mitigate it with a check
window.addEventListener('DOMContentLoaded', fetchBlogPosts);

function switchTab(tabName) {
    window.location.href = tabName;
}