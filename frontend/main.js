const BASE_URL = 'http://127.0.0.1:8000';
const API_URL = 'http://127.0.0.1:8000/api/projects';

const loginBtn = document.getElementById('login-btn');
const logoutBtn = document.getElementById('logout-btn');
const projectsWrapper = document.getElementById('projects--wrapper');

const token = localStorage.getItem('token');
if (token) {
  loginBtn.remove();
} else {
  logoutBtn.remove();
}

logoutBtn.addEventListener('click', () => {
  e.preventDefault();
  localStorage.removeItem('token');
  token = null;
  window.location = 'http://127.0.0.1:5500/login.html'
});

const getProjects = async () => {
  projectsWrapper.innerHTML = ''; // clear the html first then repopulate (kinda inefficent but it works)
  let projects;
  try {
    const projectData = await fetch(API_URL);
    projects = await projectData.json();
  } catch {
    // do nothing
  }
  console.log(projects);
  buildProjects(projects);
};

const buildProjects = projects => {
  // console.log(projectsWrapper);
  projects.forEach(project => {
    const projectCard = `
      <div class="project--card">
        <img src="${BASE_URL}${project.featured_image}">
        <div>
          <div class="card--header">
            <h3>${project.title}</h3>
            <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
            <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
          </div>
          <i>${project.vote_ratio}% positive</i>
          <p>${project.description.substring(0, 150)}</p>
        </div>
      </div>
    `;
    projectsWrapper.insertAdjacentHTML("beforeend", projectCard);
  });
  addVoteEvents();
};

const addVoteEvents = () => {
  const voteBtns = document.getElementsByClassName('vote--option');
  for (let i = 0; i < voteBtns.length; i++) {
    const btn = voteBtns[i];
    btn.addEventListener('click', e => {
      const token = localStorage.getItem('token');
      const vote = e.target.dataset.vote;
      const project = e.target.dataset.project;
      console.log(`${vote} Vote for project with id: ${project}`);
      fetch(`${API_URL}/${project}/vote/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ value: vote })
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        getProjects();
      })
      .except(err => console.error(err));
    });
  }
};

getProjects();