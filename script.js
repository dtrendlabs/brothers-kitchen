document.addEventListener('click', (e) => {
    const trigger = e.target.closest('button[aria-controls]');
    if (!trigger) return;

    const item = trigger.closest('div[data-testid^="faq-item-"]');
    if (!item) return;

    const contentId = trigger.getAttribute('aria-controls');
    const content = contentId ? document.getElementById(contentId) : null;
    
    if (!content) return;

    const isExpanded = trigger.getAttribute('aria-expanded') === 'true';

    // Function to close an item properly with animation support
    const closeItem = (el, btn) => {
        if (!el || !btn) return;
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('data-state', 'closed');
        const h3 = btn.closest('h3');
        if (h3) h3.setAttribute('data-state', 'closed');
        
        el.setAttribute('data-state', 'closed');
        // Wait for animation before hiding (matching 0.3s transition)
        setTimeout(() => {
            if (btn.getAttribute('data-state') === 'closed') {
                el.setAttribute('hidden', '');
            }
        }, 300);
    };

    // If opening a new one, close others
    if (!isExpanded) {
        const faqItems = document.querySelectorAll('div[data-testid^="faq-item-"]');
        faqItems.forEach(otherItem => {
            if (otherItem === item) return;
            const otherTrigger = otherItem.querySelector('button[aria-controls]');
            const otherContentId = otherTrigger?.getAttribute('aria-controls');
            const otherContent = otherContentId ? document.getElementById(otherContentId) : null;
            if (otherTrigger?.getAttribute('data-state') === 'open') {
                closeItem(otherContent, otherTrigger);
                otherItem.setAttribute('data-state', 'closed');
            }
        });

        // Open the clicked one
        trigger.setAttribute('aria-expanded', 'true');
        trigger.setAttribute('data-state', 'open');
        const h3 = trigger.closest('h3');
        if (h3) h3.setAttribute('data-state', 'open');
        
        content.removeAttribute('hidden');
        // Trigger reflow to ensure animation starts
        void content.offsetHeight;
        content.setAttribute('data-state', 'open');
        item.setAttribute('data-state', 'open');
    } else {
        // Toggle close if clicked again
        closeItem(content, trigger);
        item.setAttribute('data-state', 'closed');
    }
});