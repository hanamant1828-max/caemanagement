// Mobile App JavaScript - Native App Feel

console.log('Friendscars Mobile App loaded');

// Search Modal Functions
function openSearch() {
    const modal = document.getElementById('searchModal');
    if (modal) {
        modal.classList.add('active');
        setTimeout(() => {
            document.getElementById('searchInput')?.focus();
        }, 300);
    }
}

function closeSearch() {
    const modal = document.getElementById('searchModal');
    if (modal) {
        modal.classList.remove('active');
    }
}

// Close search modal on escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeSearch();
    }
});

// Prevent body scroll when modal is open
function preventScroll(e) {
    e.preventDefault();
}

// Touch feedback for buttons
document.addEventListener('DOMContentLoaded', () => {
    // Add touch feedback to interactive elements
    const touchElements = document.querySelectorAll('.btn, .category-pill, .nav-item, .chip, .header-icon-btn');
    
    touchElements.forEach(el => {
        el.addEventListener('touchstart', function() {
            this.style.transform = 'scale(0.95)';
        }, { passive: true });
        
        el.addEventListener('touchend', function() {
            this.style.transform = '';
        }, { passive: true });
    });
    
    // Smooth scroll to top on logo click
    const logo = document.querySelector('.app-logo');
    if (logo) {
        logo.addEventListener('click', (e) => {
            if (window.location.pathname === '/' || window.location.pathname.includes('marketplace')) {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        });
    }
    
    // Hide header on scroll down, show on scroll up
    let lastScroll = 0;
    const header = document.querySelector('.app-header');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll <= 0) {
            header?.classList.remove('header-hidden');
            return;
        }
        
        if (currentScroll > lastScroll && currentScroll > 100) {
            // Scrolling down
            header?.classList.add('header-hidden');
        } else {
            // Scrolling up
            header?.classList.remove('header-hidden');
        }
        
        lastScroll = currentScroll;
    }, { passive: true });
    
    // Initialize carousels with swipe support
    initSwipeCarousels();
});

// Swipe support for carousels
function initSwipeCarousels() {
    const carousels = document.querySelectorAll('.carousel');
    
    carousels.forEach(carousel => {
        let touchStartX = 0;
        let touchEndX = 0;
        
        carousel.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });
        
        carousel.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe(carousel);
        }, { passive: true });
        
        function handleSwipe(carousel) {
            const diff = touchStartX - touchEndX;
            const threshold = 50;
            
            if (Math.abs(diff) > threshold) {
                const bsCarousel = bootstrap.Carousel.getOrCreateInstance(carousel);
                if (diff > 0) {
                    // Swipe left - next
                    bsCarousel.next();
                } else {
                    // Swipe right - prev
                    bsCarousel.prev();
                }
            }
        }
    });
}

// Pull to refresh (visual only - actual refresh on release)
let pullStartY = 0;
let isPulling = false;

document.addEventListener('touchstart', (e) => {
    if (window.scrollY === 0) {
        pullStartY = e.touches[0].clientY;
        isPulling = true;
    }
}, { passive: true });

document.addEventListener('touchmove', (e) => {
    if (!isPulling) return;
    
    const pullDistance = e.touches[0].clientY - pullStartY;
    const indicator = document.querySelector('.pull-indicator');
    
    if (pullDistance > 0 && pullDistance < 150) {
        if (indicator) {
            indicator.classList.add('visible');
        }
    }
}, { passive: true });

document.addEventListener('touchend', () => {
    isPulling = false;
    const indicator = document.querySelector('.pull-indicator');
    if (indicator) {
        indicator.classList.remove('visible');
    }
}, { passive: true });

// Haptic feedback helper
function hapticFeedback(type = 'light') {
    if (navigator.vibrate) {
        switch (type) {
            case 'light':
                navigator.vibrate(10);
                break;
            case 'medium':
                navigator.vibrate(20);
                break;
            case 'heavy':
                navigator.vibrate(30);
                break;
        }
    }
}

// Share functionality
function shareVehicle(title, url) {
    if (navigator.share) {
        navigator.share({
            title: title,
            url: url
        }).catch(console.error);
    } else {
        // Fallback - copy to clipboard
        navigator.clipboard.writeText(url).then(() => {
            showToast('Link copied to clipboard!');
        }).catch(console.error);
    }
}

// Toast notification
function showToast(message, duration = 3000) {
    const existing = document.querySelector('.app-toast');
    if (existing) existing.remove();
    
    const toast = document.createElement('div');
    toast.className = 'app-toast';
    toast.innerHTML = message;
    toast.style.cssText = `
        position: fixed;
        bottom: 100px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0, 0, 0, 0.85);
        color: white;
        padding: 14px 28px;
        border-radius: 30px;
        font-size: 0.9rem;
        font-weight: 500;
        z-index: 9999;
        animation: fadeInUp 0.3s ease;
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease forwards';
        setTimeout(() => toast.remove(), 300);
    }, duration);
}

// Add CSS for toast animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translate(-50%, 20px);
        }
        to {
            opacity: 1;
            transform: translate(-50%, 0);
        }
    }
    @keyframes fadeOut {
        to {
            opacity: 0;
            transform: translate(-50%, 20px);
        }
    }
    .header-hidden {
        transform: translateY(-100%);
        transition: transform 0.3s ease;
    }
    .app-header {
        transition: transform 0.3s ease;
    }
`;
document.head.appendChild(style);

// Service Worker Registration for PWA
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(reg => console.log('Service Worker registered'))
            .catch(err => console.log('Service Worker not registered:', err));
    });
}

// Download image function
function downloadImage(vehicleId, imageName, vehicleTitle) {
    try {
        const link = document.createElement('a');
        link.href = '/static/uploads/' + imageName;
        link.download = vehicleTitle.replace(/[^a-z0-9]/gi, '_').toLowerCase() + '_' + imageName;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        showToast('Image downloaded!');
        hapticFeedback('medium');
    } catch (error) {
        console.error('Download failed:', error);
        showToast('Download failed. Please try again.');
    }
}
