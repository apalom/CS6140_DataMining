
% Prep Data
%A = table2array(A);

% Run SVD
[U,S,V] = svd(A);

% Question 1A

% Initialize Values
% k_max = 40;
% L2normAtoAk = zeros(k_max,1);
% L2normA = norm(A,2);

% for k = 1:k_max
%     Uk = U(:,1:k);
%     Sk = S(1:k,1:k);
%     Vk = V(:,1:k);
%     Ak = Uk*Sk*Vk';
%     L2normAtoAk(k) = norm(A-Ak,2);
% end


% Question 1B

% Initialize Values
% k_max = 40;
% L2normAtoAk = zeros(k_max,1);
% L2normA = norm(A,2);

% threshold = 0.1*L2normA(1);
% condition = threshold+1;
% k = 0;
% while condition >= threshold
%     k = k + 1; 
%     Uk = U(:,1:k);
%     Sk = S(1:k,1:k);
%     Vk = V(:,1:k);
%     Ak = Uk*Sk*Vk';
%     
%     L2normAtoAk(k) = norm(A-Ak,2);
%     condition(k) = L2normAtoAk(k);
%     k_smallest = k;
% end

% Question 1B

% Prep Matrix
k_max = 30;
A = A(:,1:k_max);
prevNorm = max(norm(A,2));
i = 1;

for dim1 = (1:k_max)
    for dim2 = (1:k_max)
        if dim1 ~= dim2
            Atemp = [A(:,dim1) A(:,dim2)];
            norm2d = norm(Atemp,2);
            norm2dcol(i,1) = norm2d;
            if norm2d < prevNorm
                smallestDim1 = dim1;
                smallestDim2 = dim2;
                prevNorm = norm2d;
            end
            i = i + 1;
        end
    end
end

A2_smallestNorm = [A(:,smallestDim1) A(:,smallestDim2)];

