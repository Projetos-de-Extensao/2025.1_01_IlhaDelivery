// Em ContPerfil.jsx
import React, { useState, useEffect } from "react";
import axios from '../../axios';
import "./ContPerfil.css";

function ContPerfil() {
  const [profileData, setProfileData] = useState({
    nome: '',
    endereco: '',
    telefone: '',
    email: ''
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState(''); 

  useEffect(() => {
    const fetchProfileData = async () => {
      setLoading(true);
      setError('');
      setSuccessMessage(''); 
      try {
        const response = await axios.get('/clientes/me/');
        setProfileData({
            nome: response.data.nome || '',
            endereco: response.data.endereco || '',
            telefone: response.data.telefone || '',
            email: response.data.email || '',
        });
      } catch (err) {
        console.error("Erro ao buscar dados do perfil:", err.response ? err.response.data : err.message);
        setError("Não foi possível carregar os dados do perfil.");
      } finally {
        setLoading(false);
      }
    };
    fetchProfileData();
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setProfileData(prevState => ({
      ...prevState,
      [name]: value
    }));
    setError('');
    setSuccessMessage('');
  };

  // 👇 FUNÇÃO PARA SALVAR ALTERAÇÕES 👇
  const handleSaveChanges = async (event) => {
    event.preventDefault();
    setError('');
    setSuccessMessage('');
    setLoading(true); 

    try {

      const response = await axios.patch('/clientes/me/', profileData);
      console.error("Dados não enviados:", profileData);
      
      
      setProfileData({
        nome: response.data.nome || '',
        endereco: response.data.endereco || '',
        telefone: response.data.telefone || '',
        email: response.data.email || '',
      });
      setSuccessMessage("Perfil atualizado com sucesso!");
      console.log("Perfil atualizado:", response.data);

    } catch (err) {
      console.error("Erro ao salvar alterações do perfil:", err.response ? err.response.data : err.message);
      if (err.response && err.response.data) {
        let backendErrors = err.response.data;
        let errorMsg = "Falha ao salvar. ";
        if (typeof backendErrors === 'object') {
          errorMsg += Object.keys(backendErrors).map(key => `${key}: ${backendErrors[key].join(', ')}`).join('; ');
        } else {
          errorMsg += backendErrors.detail || "Erro desconhecido do servidor.";
        }
        setError(errorMsg);
      } else {
        setError("Não foi possível salvar as alterações. Verifique sua conexão ou tente novamente.");
      }
    } finally {
      setLoading(false);
    }
  };

  if (loading && !profileData.nome) { 
    return <div className="perfil-page"><p>Carregando perfil...</p></div>;
  }

  return (
    <div className="perfil-page">
      <section className="perfil-box">
        <h3>Meu Perfil</h3>
        <p>Visualize e atualize suas informações pessoais.</p>
        <form onSubmit={handleSaveChanges}> {/* Mudado para handleSaveChanges */}
          {/* Inputs como antes, com value e onChange */}
          {/* ... (input para nome) ... */}
          <div className="form-group">
            <label className="form-label" htmlFor="nomeInput">👤 Nome:</label>
            <input type="text" id="nomeInput" name="nome" value={profileData.nome} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="enderecoInput">📍 Endereço:</label>
            <input type="text" id="enderecoInput" name="endereco" value={profileData.endereco} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="telefoneInput">📞 Telefone:</label>
            <input type="text" id="telefoneInput" name="telefone" value={profileData.telefone} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="emailInput">📧 E-mail:</label>
            <input type="email" id="emailInput" name="email" value={profileData.email} onChange={handleChange} />
          </div>

          {/* Feedback para o usuário */}
          {loading && <p>Salvando...</p>}
          {error && <p style={{ color: 'red' }}>{error}</p>}
          {successMessage && <p style={{ color: 'green' }}>{successMessage}</p>}
          
          <button type="submit" disabled={loading}> {/* Desabilita botão durante o carregamento/salvamento */}
            {loading ? 'Salvando...' : 'Salvar Alterações'}
          </button>
        </form>
      </section>
    </div>
  );
}

export default ContPerfil;