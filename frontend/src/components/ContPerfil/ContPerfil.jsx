// Em ContPerfil.jsx
import React, { useState, useEffect } from "react";
import axios from '../../axios';
import "./ContPerfil.css"; // O CSS melhorado

function ContPerfil() {
  const [profileData, setProfileData] = useState({
    nome: '',
    endereco: '',
    telefone: '',
    email: ''
  });
  const [loading, setLoading] = useState(true); // Inicia como true para mostrar o loader
  const [isSaving, setIsSaving] = useState(false);
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  // 👇 O BLOCO QUE FALTAVA ESTÁ AQUI 👇
  // Este useEffect é executado uma vez, quando o componente é montado.
  // Sua função é buscar os dados iniciais do perfil no servidor.
  useEffect(() => {
    const fetchProfileData = async () => {
      setLoading(true); // Garante que o estado de loading esteja ativo
      setError('');
      try {
        const response = await axios.get('/clientes/me/');
        // Preenche o estado com os dados recebidos da API
        setProfileData({
            nome: response.data.nome || '',
            endereco: response.data.endereco || '',
            telefone: response.data.telefone || '',
            email: response.data.email || '',
        });
      } catch (err) {
        console.error("Erro ao buscar dados do perfil:", err.response ? err.response.data : err.message);
        setError("Não foi possível carregar os dados do seu perfil. Tente recarregar a página.");
      } finally {
        // ESSA É A LINHA MAIS IMPORTANTE:
        // Independentemente de sucesso ou falha, o loading termina aqui.
        setLoading(false);
      }
    };

    fetchProfileData();
  }, []); // O array vazio [] garante que isso rode apenas uma vez.

  const handleChange = (event) => {
    const { name, value } = event.target;
    setProfileData(prevState => ({
      ...prevState,
      [name]: value
    }));
    setError('');
    setSuccessMessage('');
  };

  const handleSaveChanges = async (event) => {
    event.preventDefault();
    setError('');
    setSuccessMessage('');
    setIsSaving(true);

    try {
      const response = await axios.patch('/clientes/me/', profileData);
      setProfileData(response.data);
      setSuccessMessage("Perfil atualizado com sucesso!");
    } catch (err) {
      console.error("Erro ao salvar alterações do perfil:", err.response ? err.response.data : err.message);
      setError("Não foi possível salvar as alterações.");
    } finally {
      setIsSaving(false);
    }
  };

  // Enquanto estiver carregando os dados iniciais, mostra a mensagem
  if (loading) {
    return (
      <div className="perfil-page">
        <p className="feedback-message loading">Carregando perfil...</p>
      </div>
    );
  }

  // Após carregar, mostra o formulário
  return (
    <div className="perfil-page">
      <section className="perfil-box">
        <h3>Meu Perfil</h3>
        <p>Visualize e atualize suas informações pessoais.</p>

        <form onSubmit={handleSaveChanges}>
          <div className="form-group">
            <label className="form-label" htmlFor="nomeInput">👤 Nome:</label>
            <input className="form-input" type="text" id="nomeInput" name="nome" value={profileData.nome} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="enderecoInput">📍 Endereço:</label>
            <input className="form-input" type="text" id="enderecoInput" name="endereco" value={profileData.endereco} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="telefoneInput">📞 Telefone:</label>
            <input className="form-input" type="text" id="telefoneInput" name="telefone" value={profileData.telefone} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="emailInput">📧 E-mail:</label>
            <input className="form-input" type="email" id="emailInput" name="email" value={profileData.email} onChange={handleChange} />
          </div>

          {isSaving && <p className="feedback-message loading">Salvando...</p>}
          {error && <p className="feedback-message error">{error}</p>}
          {successMessage && <p className="feedback-message success">{successMessage}</p>}

          <button type="submit" className="submit-btn" disabled={isSaving}>
            {isSaving ? 'Salvando...' : 'Salvar Alterações'}
          </button>
        </form>
      </section>
    </div>
  );
}

export default ContPerfil;