---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/snippets/callout.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/snippets/callout.mdx
---
export const Callout = ({ title, children }) => (
  
    
      
      
        {title && {title}}
        {children}
      
    
  
);

export const Warning = ({ title, children }) => (
  
    
      
      
        {title && {title}}
        {children}
      
    
  
);

export const Danger = ({ title, children }) => (
  
    
      
      
        {title && {title}}
        {children}
      
    
  
);
