% THIS IS MATLAB CODE
% Michael S. Branicky

init = 50;
jinit = 55;
igoal = 75;
jgoal = 70;

obs=zeros(100,100); % initialize to "no obstacles"
for i=1:100,
  for j=1:100,
    if i<50,    % rear of bugtrap
      d=abs(i-51)+abs(j-50);
      if d==50, obs(i,j)=1;  end;
    else        % front of bugtrap
      if j>50,  % upper lobe
        d=abs(i-50)+abs(j-75);
        if d==24, obs(i,j)=1; end;
      end;
      if j<50,  % lower lobe
        d=abs(i-50)+abs(j-25);
        if d==24, obs(i,j)=1; end;
      end;
    end;
  end;
end;

spy(obs)
